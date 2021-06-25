/**
  *
  * main() will be run when you invoke this action
  *
  * @param Cloud Functions actions accept a single parameter, which must be a JSON object.
  *
  * @return The output of this action, which must be a JSON object.
  *
  */

function main1(params) {
  if (params.dealerId) {
    return {
      "query": {"selector": {"id": parseInt(params.dealerId, 10)}}
    };
  };
  return {
    "query": {"selector": {"st": params.state}}
  };
}



function main2(params) {
  return {
    entries: params.docs.map(doc => { return {
      full_name: doc.full_name,
      short_name: doc.short_name,
      id: doc.id,
      city: doc.city,
      state: doc.state,
      st: doc.st,
      address: doc.address,
      zip: doc.zip,
      lat: doc.lat,
      long: doc.long,
    }})
  };
}