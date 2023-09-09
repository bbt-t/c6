from dataclasses import dataclass

from .models import BlogPost
from .tools import generate_number_image


@dataclass
class HomePageCtx:
    """
    Context for homepage.
    """

    total_mailings: int
    active_mailings: int
    unique_clients: int

    random_posts: BlogPost

    def __post_init__(self) -> None:
        """
        Generate and set images.
        """
        self.total_mailings_img = generate_number_image(self.total_mailings)
        self.active_mailings_img = generate_number_image(self.active_mailings)
        self.unique_clients_img = generate_number_image(self.unique_clients)
