const mongoose=require('mongoose');
const uri = 'mongodb+srv://pranavdabade:W1mnUZe4AKjaptHf@heartinsights.gbg20l6.mongodb.net/?appName=heartinsights'

const connectToMongo=async()=>{
    try
    {
        await mongoose.connect(uri);
        console.log("Db connected Successfully")
    }
    catch(error)
    {
        console.error('Error connecting to Mongodb',error);
    }
}
module.exports=connectToMongo;