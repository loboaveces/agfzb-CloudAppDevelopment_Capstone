#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys


def main1(params):
    return {"query": {"selector": {"dealership": int(params["dealerId"])}}}


def main2(params):
    return {
        "entries": list(
            map(
                lambda doc: {
                    "id": doc.get("id"),
                    "name": doc.get("name"),
                    "dealership": doc.get("dealership"),
                    "review": doc.get("review"),
                    "purchase": doc.get("purchase"),
                    "purchase_date": doc.get("purchase_date"),
                    "car_make": doc.get("car_make"),
                    "car_model": doc.get("car_model"),
                    "car_year": doc.get("car_year"),
                },
                params.get("docs")
            )
        )
    }