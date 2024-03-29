const express = require("express");
const bodyParser = require("body-parser");

const app = express();

app.set("view engine", "ejs");

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

app.get("/", function(req, res) {
    //res.send("<h1>Hello</h1>");
    //res.sendFile(__dirname + "/index.html");
    res.render("index.ejs", {pageName: "Home"});

});

app.get("/webdev", function(req, res) {
    //res.send("<h1>Hello</h1>");
    //res.sendFile(__dirname + "/index.html");
    res.render("webdev.ejs", {pageName: "Home"});
});
app.get("/webdev/anatomy", function(req, res) {
    res.render("webdev/anatomy.ejs", {pageName: "Anatomy Of This Website"});

});

app.get("/webdev/portfolio", function(req, res) {
    res.render("webdev/portfolio.ejs", {pageName: "My Portfolio"});

});

app.get("/python", function(req, res) {
    res.render("python/python.ejs", {pageName: "Python Programming"});

});

app.get("/camping", function(req, res) {
    res.render("camping/camping.ejs", {pageName: "Camping & Hiking"});

});
app.get("/camping/gear", function(req, res) {
    res.render("camping/gear.ejs", {pageName: "Camping Gear"});

});
app.get("/camping/places", function(req, res) {
    res.render("camping/places.ejs", {pageName: "Favourite Places"});

});

app.get("/sight", function(req, res) {
    res.render("sight.ejs", {pageName: "Sight Loss"});

});




app.get("/webdev/examples/bridge", function(req, res) {
    res.render("webdev/examples/bridge/bridge.ejs", {pageName: "My Portfolio"});

});

app.get("/webdev/examples/reimagined", function(req, res) {
    res.render("webdev/examples/reimagined/reimagined.ejs", {pageName: "My Portfolio"});

});

app.get("/webdev/examples/blog-site", function(req, res) {
    res.render("webdev/examples/blog-site.ejs", {pageName: "My Portfolio"});

});

app.get("/webdev/examples/reimagined/python", function(req, res) {
    res.render("webdev/examples/reimagined/python.ejs", {pageName: "My Portfolio"});

});
    app.get("/webdev/examples/reimagined/places", function(req, res) {
        res.render("webdev/examples/reimagined/places.ejs", {pageName: "My Portfolio"});

    });



app.listen(process.env.PORT || 7000, function(){

    console.log("server started on port 7000");

});