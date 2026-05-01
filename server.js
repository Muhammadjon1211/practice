// NodeJS EXPRESS NESTJS
// Python Django FastAPI
const express = require('express')
const app = express()

//Traditional
app.get('/', (req, res) => {
  res.send('<h1>Hello World!</h1>')
})

//Rest API
app.get('/rest', (req, res) => {
  res.json({name: "Marco", age:21})
})

app.listen(3000, () => {
  console.log("Backend server is running in port 3000")
})