# Purpose
This API generate a list of random number within a given range

# How to use
Connect to https://ash-random-api.herokuapp.com/"quantity"/"min"/"max" using get method  <br />
For example if you want 5 random number in the range 1 to 10, then the url would be: https://ash-random-api.herokuapp.com/5/1/10

JavaScript client example:
```
async function getData() {
  const response = await fetch('https://ash-random-api.herokuapp.com/5/1/10', {method: "GET"})
  const data = await response.json()
  return data
}
```
The response would be:
```
{"answer":[7,4,5,8,3]}
```
