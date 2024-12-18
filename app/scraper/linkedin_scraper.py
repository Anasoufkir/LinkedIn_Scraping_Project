from playwright.sync_api import sync_playwright
from app.scraper.utils import handle_rate_limit, parse_profile_data

class LinkedInScraper:
    def __init__(self, base_url="https://www.linkedin.com"):
        self.base_url = base_url

    def start_browser(self):
        # Démarre le navigateur Playwright
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=True)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def close_browser(self):
        # Ferme le navigateur
        if hasattr(self, "browser"):
            self.browser.close()

    def login(self, username: str, password: str):
        """Se connecter à LinkedIn."""
        self.page.goto(f"{self.base_url}/login")
        self.page.fill("input#username", username)
        self.page.fill("input#password", password)
        self.page.click("button[type='submit']")
        # Vérifier si la connexion a réussi
        if "feed" not in self.page.url:
            raise Exception("Login failed. Please check your credentials.")

    def scrape_profile(self, profile_url: str) -> dict:
        """Scraper un profil LinkedIn donné."""
        self.page.goto(profile_url)
        handle_rate_limit(self.page)

        # Extraire les données du profil
        profile_data = parse_profile_data(self.page.content())
        return profile_data

    def scrape_company(self, company_url: str) -> dict:
        """Scraper une entreprise LinkedIn donnée."""
        self.page.goto(company_url)
        handle_rate_limit(self.page)

        # Extraire les données de l'entreprise
        # Exemple de parse spécifique
        return {
            "name": self.page.locator(".org-top-card-summary__title").text_content(),
            "sector": self.page.locator(".org-top-card-summary__industry").text_content(),
            "location": self.page.locator(".org-top-card-summary__headquarters").text_content(),
        }

    def scrape_jobs(self, jobs_url: str) -> list[dict]:
        """Scraper les offres d'emploi."""
        self.page.goto(jobs_url)
        handle_rate_limit(self.page)

        # Exemple d'extraction des données
        jobs = []
        job_elements = self.page.locator(".jobs-search-results__list-item")
        for job in job_elements:
            jobs.append({
                "title": job.locator(".job-card-list__title").text_content(),
                "company": job.locator(".job-card-container__company-name").text_content(),
                "location": job.locator(".job-card-container__metadata-item").text_content(),
            })
        return jobs
