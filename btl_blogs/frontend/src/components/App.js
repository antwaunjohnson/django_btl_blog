import React, { Component } from "react";
import ReactDOM from "react-dom";
import Home from "./Home";
import Navigation from "./Navigation/Navbar";

class App extends Component {
  render() {
    return (
      <div>
        {/**
         * Route home
         * / -> path
         */}
        <Home />
        {/**
         * Route login
         * /login -> path
         */}
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
