import React from 'react';
import ReactDOM from 'react-dom';
import '../css/admin.css';
import '../css/basic.css';

export class AdminPage extends React.Component {
    Header = () => {
        return <header className={'header'}>
            <h2 className={'header-title'}>Заявки</h2>
        </header>;
    }

    Main = () => {
        return <main className={'Main'}></main>;
    }

    render() {
        return <div>
            {this.Header()}
            {this.Main()}
        </div>;
    }
}