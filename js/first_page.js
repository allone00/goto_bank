import React from 'react';
import '../css/auth.css';
import '../css/basic.css';

export class FirstPage extends React.Component {
    Main = () => {
        return <main className={'main'}>
            {this.Inner_container()}</main>;
    }
    ContainerTitle = () => {
        return <h1 className={'Container_title'}>GoToCredit</h1>;
    }

    ContainerText = () => {
        return <h2 className={'Container_text'}>Всего 3 шага до вашей мечты!</h2>;
    }

    Footer = () => {
        return <footer className={'footer'}>{this.Footer_text()}</footer>;
    }

    Footer_text = () => {
        return <h3 className={'footer_text'}>По всем вопросам писать сюда - @tvorogme</h3>;
    }

    AuthButton = () => {
        return <a className={'AuthButton'} value={'auth'}
                  href={"https://stonks.goto.msk.ru/o/authorize/?state=random_state_string&client_id=M2mY5d4b6NcVKxr2XqKXSxZgpk78WK6ZaU3IxYDd&response_type=code"}>
            Auth!
        </a>;
    }

    Inner_container = () => {
        return <div className={'Inner_container'}>
            {this.ContainerTitle()}
            {this.AuthButton()}
        </div>;
    }

    render() {
        return (
            <div>
                {this.Main()}
                {this.Footer()}
            </div>
        );
    }
}

