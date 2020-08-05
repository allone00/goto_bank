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
import {MainPage} from "./main_page";

class App extends React.Component {
    render() {
        return <Router>
        <Switch>

            <Route path={'/form'} component={MainPage}/>
            <Route path={'/'} component={FirstPage}/>
        </Switch>
        </Router>;
    }
}


ReactDOM.render(<App/>, document.getElementById('cool'));

