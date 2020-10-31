require('dotenv').config();
const express = require('express');
const router = express.Router();
const BigMac = require('../../models/BigMac');
const db = require('../../models');

// GET /api/bigmac
// Display all prices
router.get('/', (req, res) => {
    db.BigMac.find()
    .then(bigmac => {
        res.send(bigmac)
    })
    .catch(err => console.log(err))
})

// Sort by most expensive
router.get('/most', (req, res) => {
    db.BigMac.find().sort({price: -1})
    .then(bigmac => {
        res.send(bigmac)
    })
    .catch(err => console.log(err))
})

// Sort by least expensive
router.get('/least', (req, res) => {
    db.BigMac.find().sort({price: 1})
    .then(bigmac => {
        res.send(bigmac)
    })
    .catch(err => console.log(err))
})

// Search for a certain city/state
router.get('/:id', (req, res) => {
    db.BigMac.find({
        location: /req.params.id/i
    })
    .then(bigmac => {
        res.send(bigmac)
    })
    .catch(err => console.log(err))
})

router.post('/', (req, res) => {
    const newBigMac = new BigMac({
        location: req.body.location,
        price: req.body.price
    })
    newBigMac.save()
    .then(createdBigMac => {
        res.json(createdBigMac)
    })
    .catch(err => console.log(err))
})

router.delete('/:id', (req,res) => {
    db.BigMac.deleteOne({
        _id: req.params.id
    })
    .then(res.send('deleted'))
    .catch(err => console.log(err))
})

module.exports = router