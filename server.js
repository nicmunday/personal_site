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
    //res.send("<h1>Hello</h1>");
    //res.sendFile(__dirname + "/index.html");
    res.render("webdev/anatomy.ejs", {pageName: "Anatomy Of This Website"});

});

app.get("/webdev/portfolio", function(req, res) {
    //res.send("<h1>Hello</h1>");
    //res.sendFile(__dirname + "/index.html");
    res.render("webdev/portfolio.ejs", {pageName: "Web Design Portfolio"});

});

app.get("/python", function(req, res) {
    //res.send("<h1>Hello</h1>");
    //res.sendFile(__dirname + "/index.html");
    res.render("python.ejs", {pageName: "Python Programming"});

});

app.get("/camping", function(req, res) {
    //res.send("<h1>Hello</h1>");
    //res.sendFile(__dirname + "/index.html");
    res.render("camping.ejs", {pageName: "Camping And Hiking"});

});
app.get("/camping/gear", function(req, res) {
    //res.send("<h1>Hello</h1>");
    //res.sendFile(__dirname + "/index.html");
    res.render("camping/gear.ejs", {pageName: "Camping Gear"});

});
app.get("/camping/places", function(req, res) {
    //res.send("<h1>Hello</h1>");
    //res.sendFile(__dirname + "/index.html");
    res.render("camping/places.ejs", {pageName: "My Favourite Places"});

});

app.get("/sight", function(req, res) {
    //res.send("<h1>Hello</h1>");
    //res.sendFile(__dirname + "/index.html");
    res.render("sight.ejs", {pageName: "Sight Loss"});

});

app.listen(process.env.PORT || 3000, function(){

    console.log("server started on port 3000");

});