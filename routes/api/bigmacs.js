require('dotenv').config();
const express = require('express');
const router = express.Router();
const BigMac = require('../../models/BigMac');

// GET /api/bigmac
// Display all prices
router.get('/', (req, res) => {
    BigMac.find()
    .then(bigmac => {
        res.send(bigmac)
    })
    .catch(err => console.log(err))
})


module.exports = router