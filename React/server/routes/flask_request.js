const postFlaskData = require('../controllers/flask');

const express = require('express');

const router = express.Router()

router.post("/predict", postFlaskData)

module.exports = router