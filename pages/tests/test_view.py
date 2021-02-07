import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed

# assertsTemplateUsed : Vamos garatir que a template que a gente quer
# esta sendo usada
# resolve dada uma url , ele me devolve uma view
# reserve dada uma view , ele me devolve uma url


@pytest.fixture  # Reultiza a home_response em outros teste
def home_response(client):
    return client.get(reverse("pages:home"))

# client = Chrome


@pytest.fixture
def about_response(client):
    return client.get(reverse("pages:about"))


class TestHomePageView:
    def test_reverse_resolve(self):
        assert reverse("pages:home") == "/"
        assert resolve("/").view_name == "pages:home"

    def test_status_code(self, home_response):
        assert home_response.status_code == 200

    def test_template(self, home_response):
        assertTemplateUsed(home_response, "home.html")


class TestAboutView:
    def test_reverse_resolve(self):
        assert reverse("pages:about") == "/about/"
        assert resolve("/about/").view_name == "pages:about"

    def test_status_code(self, about_response):
        assert about_response.status_code == 200

    def test_template(self, about_response):
        assertTemplateUsed(about_response, "about.html")
