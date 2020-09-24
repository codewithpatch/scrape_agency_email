from dataclasses import dataclass
from typing import Optional


@dataclass
class AgencyScrapedDetails:
    agency_name: str
    agecy_health_direct_url: Optional[str] = None
    agency_email: Optional[str] = None

