// index.js

/**
 * Required External Modules
*/

const express = require("express");
const path = require("path");
const fs = require('fs');
const {spawn} = require("child_process");


/**
 * App Variables
*/

const app = express();
const port = process.env.PORT || "5000";
const host = process.env.host || "127.0.0.1";
const tabsize = 4;
const JSONFile = JSON.parse(fs.readFileSync(path.resolve(__dirname, "json/macos.json")));


/**
 * App Configuration
*/

app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");
app.use(express.static(path.join(__dirname, "public")));



/**
 * Route Definitions
*/

// Home
app.get("/", (req, res) => {

    // Source: https://medium.com/swlh/run-python-script-from-node-js-and-send-data-to-browser-15677fcf199f
    
    var parsedJSON = [];

    const python = spawn('python3', ['python/parse-json.py']);

    python.stdout.on('data', function (data) {
        parsedJSON.push(data);
    });
   
    python.on('close', (code) => {
        res.render( "index", { 
            title: "JSON", 
            heading: "Raw JSON from file", 
            prettyprint: JSON.stringify(JSONFile, null, tabsize), 
            parsed: parsedJSON.join("")
        });
    });
    
});



/**
 * Server Activation
*/

app.listen(port, () => {
    console.log(`Listening to requests on http://${host}:${port}`);
});