express = require('express')
dotenv = require("dotenv")
cors = require('cors')
const flaskRequestRouter = require('./routes/flask_request')
const app = express()
const port = 3000


app.use(cors())
app.use(express.json())
app.use('/api', flaskRequestRouter)

app.get('/', (req,res) =>{
    res.send('Hello baby').status(200)
})
app.get('/test', (req, res)=>{
    res.send("I am now testtion").status(200)
})

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`)
})