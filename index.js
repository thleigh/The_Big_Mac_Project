const mongoose = require('mongoose');

// MONGO CONNECTION
mongoose.connect(process.env.ATLAS_URI || process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    useUnifiedTopology: true
});

app.listen(process.env.PORT || 3000)

// Mongoose connection object
const db = mongoose.connection;

// set up an event listener to fire once when the connection 'opens'
// console log what port it's running on
db.once('open', () => {
    console.log(`Connected to MongoDB at ${db.host}:${db.port}`)
});

db.on('error', (error) => {
    console.log(`Database error\n${error}`)
});

module.exports.BigMac = require('./models/BigMac');