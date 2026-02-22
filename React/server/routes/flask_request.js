express = require('express');
const router = express.Router()

router.post('predict', async (req, res) => {
    const data = req.body
    try{
        const response = await fetch ("http://localhost:8000/predict", {
            method : 'POST',
            headers :{
                'content-type' : 'application/json'
            },
            body : JSON.stringify(data)
        })
            const result = await response.json()
            res.json(result)
            }

     catch (error){
        console.error('Error:', error)
        res.status(500).json({ error: 'An error occurred' })
    }})

    module.exports = router