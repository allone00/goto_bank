import React from 'react';
import ReactDOM from 'react-dom';

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
import {AdminPage} from './admin';

class App extends React.Component {
    render() {
        return <Router>
            <Switch>
                <Route path={'/admin'} component={AdminPage}/>
                <Route path={'/form'} component={MainPage}/>
                <Route path={'/'} component={FirstPage}/>
            </Switch>
        </Router>;
    }
}


ReactDOM.render(<App/>, document.getElementById('cool'));

