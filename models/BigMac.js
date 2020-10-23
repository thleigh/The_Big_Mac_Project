const mongoose = require('mongoose');
const Schema = mongoose.Schema; 

const BigMacSchema = new Schema ({
  
    City: {
        type: String
    },
    State: {
        type: String
    },
    Price: {
        type: Number
    }
})

module.exports = mongoose.model('BigMac', BigMacSchema);