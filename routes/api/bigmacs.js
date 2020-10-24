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

router.post('/', (req, res) => {
    const newBigMac = new BigMac({
        city: req.body.city,
        state: req.body.state,
        price: req.body.price
    })
    newBigMac.save()
    .then(createdBigMac => {
        res.json(createdBigMac)
    })
    .catch(err => console.log(err))
})


module.exports = router