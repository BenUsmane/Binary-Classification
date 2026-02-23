const postFlaskData = require('../controllers/flask');

const express = require('express');

const router = express.Router()

router.post("/predict", postFlaskData)
router.get("/", (req, res) =>{
    res.send("Hello baby").status(200)
})

module.exports = router