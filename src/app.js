const { MongoClient } = require('mongodb')
const express = require("express")
const bodyParser = require('body-parser')

const url = process.env.MONGODB_URL
const port = process.env.PORTUSED
// new change at line 7
const client = new MongoClient(url)
const dbName = 'xharktank'

client.connect()
const db = client.db(dbName)
const pitches = db.collection('pitches')
const offers = db.collection('offers')

const app = express()
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: true}))


app.post('/pitches', async (req, res) => {
    try {
        let pitchList = await pitches.find({}).toArray()
        let pid = pitchList.length + 1
        
        const pitch = {
            id: pid.toString(),
            entrepreneur: req.body.entrepreneur,
            pitchTitle: req.body.pitchTitle,
            pitchIdea: req.body.pitchIdea,
            askAmount: req.body.askAmount,
            equity: req.body.equity
        }

        if (!pitch.entrepreneur || !pitch.pitchTitle || !pitch.pitchIdea || !pitch.askAmount || !pitch.equity) {
            throw new Error("All details required")
        }

        if (pitch.entrepreneur == "" || pitch.pitchTitle == "" || pitch.pitchIdea == "" || pitch.askAmount < 0 || pitch.equity < 0 || pitch.equity > 100) {
            throw new Error("Invalid details")
        }

        await pitches.insertOne(pitch)

        let response = {
            id: pid.toString()
        }
        res.status(201).send(response)
    }
    catch (e) {
        res.status(400).end()
    }
})


app.post('/pitches/:pid/makeOffer', async (req, res) => {
    try {
        let pitch = await pitches.findOne({id: req.params.pid})
        if (!pitch) {
            res.status(404).end()
        }
        else {
            let offerList = await offers.find({}).toArray()
            let oid = offerList.length + 1

            const offer = {
                id: oid.toString(),
                pitchId: req.params.pid,
                investor: req.body.investor,
                amount: req.body.amount,
                equity: req.body.equity,
                comment: req.body.comment
            }
            if (!offer.investor || !offer.amount || !offer.equity || !offer.comment) {
                throw new Error("All details required")
            }
            if (offer.investor == "" || offer.amount < 0 || offer.equity < 0 || offer.equity > 100 || offer.comment == "") {
                throw new Error("Invalid details")
            }

            await offers.insertOne(offer)

            let response = {
                id: oid.toString()
            }
            res.status(201).send(response)
        }
    }
    catch (e) {
        res.status(400).end()
    }
})


app.get('/pitches', async (req, res) => {
    try {
        let pitchList = await pitches.find({}).toArray()
        pitchList.sort((p1, p2) => parseInt(p2.id) - parseInt(p1.id))

        let response = []
        for (var p of pitchList) {
            let offerList = await offers.find({pitchId: p.id}).toArray()
            let tempOffers = []
            for (var o of offerList) {
                let tempOffer = {
                    id: o.id,
                    investor: o.investor,
                    amount: o.amount,
                    equity: o.equity,
                    comment: o.comment
                }
                tempOffers.push(tempOffer)
            }
            let temp = {
                id: p.id,
                entrepreneur: p.entrepreneur,
                pitchTitle: p.pitchTitle,
                pitchIdea: p.pitchIdea,
                askAmount: p.askAmount,
                equity: p.equity,
                offers: tempOffers
            }
            response.push(temp)
        }

        res.status(200).send(response)
    }
    catch (e) {
        res.status(400).end()
    }
})


app.get('/pitches/:pid', async (req, res) => {
    try {
        let pitch = await pitches.findOne({id: req.params.pid})
        if (!pitch) {
            res.status(404).end()
        }
        else {
            let offerList = await offers.find({pitchId: req.params.pid}).toArray()
            let tempOffers = []
            for (var o of offerList) {
                let tempOffer = {
                    id: o.id,
                    investor: o.investor,
                    amount: o.amount,
                    equity: o.equity,
                    comment: o.comment
                }
                tempOffers.push(tempOffer)
            }
            let response = {
                id: req.params.pid,
                entrepreneur: pitch.entrepreneur,
                pitchTitle: pitch.pitchTitle,
                pitchIdea: pitch.pitchIdea,
                askAmount: pitch.askAmount,
                equity: pitch.equity,
                offers: tempOffers
            }
            res.status(200).send(response)
        }
    }
    catch (e) {
        res.status(400).end()
    }
})


app.listen(port, () => {
    console.log('Server is running on port ' + port)
})