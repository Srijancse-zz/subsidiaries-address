# subsidiaries-address

Currently I am using Google Places API to find the addresses. But it is not giving the results as I expected. Currently if an input parameter is just a company without a location, say Spendesk, it would give no results. But if you type Spendesk, Europe it shows the result. For eg, if I give an input of Econocom, Europe, it does show the results but not all the locations it should. To overcome this problem, what I could have done is :

- Make a list of arrays with the name of countries, for eg, Italy, Spain, France, UK, Belgium and then request with Econocom Italy, Econocom Spain etc and then combined the results.

Currently it outputs the result as a json and `formatted_address` parameter has the address associated. 
