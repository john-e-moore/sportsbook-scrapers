from dataclasses import dataclass, field
from typing import List, Any, Dict
from datetime import datetime
import json

from dataclasses import dataclass, field
from typing import List, Any, Dict
import json

@dataclass
class Outcome:
    providerOutcomeId: str
    providerId: int
    providerOfferId: str
    label: str
    oddsAmerican: str
    oddsDecimal: float
    oddsDecimalDisplay: str
    oddsFractional: str
    line: float
    participant: str
    participantType: str
    main: bool
    sortOrder: int
    tags: List[str]
    participants: List[Dict[str, Any]]

@dataclass
class Offer:
    providerOfferId: str
    eventId: str
    eventGroupId: str
    label: str
    isSuspended: bool
    isOpen: bool
    offerSubcategoryId: int
    isSubcategoryFeatured: bool
    betOfferTypeId: int
    providerCriterionId: str
    outcomes: List[Outcome]
    offerSequence: int
    source: str
    displayGroupId: str
    main: bool
    dkPlayerId: str
    playerNameIdentifier: str
    tags: List[str]
    categoryId: int
    categoryName: str
    subcategoryId: int
    subcategoryName: str

    def flatten(self) -> Dict[str, Any]:
        flattened = {
            "providerOfferId": self.providerOfferId,
            "eventId": self.eventId,
            "eventGroupId": self.eventGroupId,
            "label": self.label,
            "isSuspended": self.isSuspended,
            "isOpen": self.isOpen,
            "offerSubcategoryId": self.offerSubcategoryId,
            "isSubcategoryFeatured": self.isSubcategoryFeatured,
            "betOfferTypeId": self.betOfferTypeId,
            "providerCriterionId": self.providerCriterionId,
            "offerSequence": self.offerSequence,
            "source": self.source,
            "displayGroupId": self.displayGroupId,
            "main": self.main,
            "dkPlayerId": self.dkPlayerId,
            "playerNameIdentifier": self.playerNameIdentifier,
            "tags": self.tags,
            "categoryId": self.categoryId,
            "categoryName": self.categoryName,
            "subcategoryId": self.subcategoryId,
            "subcategoryName": self.subcategoryName,
        }
        
        for outcome in self.outcomes:
            label = outcome.label.lower()
            flattened[f"{label}_oddsAmerican"] = outcome.oddsAmerican
            flattened[f"{label}_oddsDecimal"] = outcome.oddsDecimal
            flattened[f"{label}_oddsDecimalDisplay"] = outcome.oddsDecimalDisplay
            flattened[f"{label}_oddsFractional"] = outcome.oddsFractional
            flattened[f"{label}_line"] = outcome.line
            flattened[f"{label}_participant"] = outcome.participant
            flattened[f"{label}_participantType"] = outcome.participantType
            flattened[f"{label}_main"] = outcome.main
            flattened[f"{label}_sortOrder"] = outcome.sortOrder
            flattened[f"{label}_tags"] = outcome.tags
            flattened[f"{label}_participants"] = outcome.participants

        return flattened

@dataclass
class Offers:
    offers: List[Offer] = field(default_factory=list)

    def flatten_all(self) -> List[Dict[str, Any]]:
        return [offer.flatten() for offer in self.offers]
    
    def add_timestamp(self) -> None:
        timestamp = datetime.now().isoformat()
        for offer in self.offers:
            offer.timestamp = timestamp

    def to_json(self) -> str:
        return json.dumps(self.flatten_all(), indent=4)

"""
# Example usage with the given JSON data (assuming it's loaded into a variable `data`)
# Load the JSON data
with open('/mnt/data/bronze_sample.json', 'r') as f:
    data = json.load(f)

# Parse the data into Offer objects
offers_list = []
for category in data['eventGroup']['offerCategories']:
    if 'offerSubcategoryDescriptors' in category:
        for subcategory in category['offerSubcategoryDescriptors']:
            for offer in subcategory['offerSubcategory']['offers'][0]:  # Assuming single offer list
                outcomes = [Outcome(**outcome) for outcome in offer['outcomes']]
                offer_obj = Offer(
                    providerOfferId=offer['providerOfferId'],
                    eventId=offer['eventId'],
                    eventGroupId=offer['eventGroupId'],
                    label=offer['label'],
                    isSuspended=offer['isSuspended'],
                    isOpen=offer['isOpen'],
                    offerSubcategoryId=offer['offerSubcategoryId'],
                    isSubcategoryFeatured=offer['isSubcategoryFeatured'],
                    betOfferTypeId=offer['betOfferTypeId'],
                    providerCriterionId=offer['providerCriterionId'],
                    outcomes=outcomes,
                    offerSequence=offer['offerSequence'],
                    source=offer['source'],
                    displayGroupId=offer['displayGroupId'],
                    main=offer['main'],
                    dkPlayerId=offer['dkPlayerId'],
                    playerNameIdentifier=offer['playerNameIdentifier'],
                    tags=offer['tags'],
                    categoryId=category['offerCategoryId'],
                    categoryName=category['name'],
                    subcategoryId=subcategory['subcategoryId'],
                    subcategoryName=subcategory['name']
                )
                offers_list.append(offer_obj)

# Create the Offers object
offers = Offers(offers=offers_list)

# Flatten all offers and convert to JSON
flattened_offers = offers.flatten_all()
offers_json = offers.to_json()

# Print the JSON representation of the flattened offers
print(offers_json)
"""
