const mongoose = require('mongoose');
const Schema = mongoose.Schema; 

const BigMacSchema = new Schema ({
    location: {
        type: String
    },
    price: {
        type: Number
    },
});

module.exports = mongoose.model('BigMac', BigMacSchema);