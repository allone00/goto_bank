import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import '../css/auth.css';
import '../css/basic.css';
import '../css/login.css';

import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    useRouteMatch,
    useParams
} from "react-router-dom";
import {FirstPage} from "./first_page";



ReactDOM.render(<FirstPage/>, document.getElementById('cool'));

