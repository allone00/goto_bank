import React from 'react';
import ReactDOM from 'react-dom';
import '../css/auth.css';
import '../css/basic.css';

function Submit() {
    let formData = new FormData();

    const send_message = (formData) => { fetch('/api/qwerty', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData

    })
        .then(response => console.log('message send with fetch!'))
        .catch(error => console.log(error))
    };

    formData.append('username', document.querySelector('.UsernameInput').value);
    formData.append('mac_address', document.querySelector('.MacInput').value);
    formData.append('mail_input', document.querySelector('.MailInput').value);
    formData.append('amount_input', document.querySelector('.AmountInput').value);

    send_message(JSON.stringify(formData));

    document.querySelector('.UsernameInput').value = '';
    document.querySelector('.MacInput').value = '';
    document.querySelector('.MailInput').value = '';
    document.querySelector('.AmountInput').value = '';

}


export class FirstPage extends React.Component {
    constructor(props) {
        super(props);
    }

    Main = () => {
        return <main className={'main'}>
            {this.Inner_container()}</main>;
    }
    ContainerTitle = () => {
        return <h1 className={'container_title'}>GoToCredit</h1>;
    }

    ContainerText = () => {
        return <h2 className={'container_text'}>Всего 3 шага до вашей мечты!</h2>;
    }

    Footer = () => {
        return <footer className={'footer'}>{this.Footer_text()}</footer>;
    }

    Footer_text = () => {
        return <h3 className={'footer_text'}>По всем вопросам писать сюда - @tvorogme</h3>;
    }

    RequestButton = () => {
        return <a className={'RequestButton'} value={'register'} onClick={Submit}
                  href={"https://stonks.goto.msk.ru/o/authorize/?state=random_state_string&client_id=M2mY5d4b6NcVKxr2XqKXSxZgpk78WK6ZaU3IxYDd&response_type=code"}>
            Click!
        </a>;
    }

    Inner_container = () => {
        return <div className={'inner_container'}>
            {this.ContainerTitle()}
            {this.ContainerText()}
            {this.Form()}
        </div>;
    }

    Form = () => {
        return (<form className={'form'} method={'post'}>
            <label htmlFor={'Username_field'} className={'UsernameForm'}>ФИО: <br/>
                <input type={'text'} id={'Username_field'} name={'Username_field'} className={'UsernameInput'} placeholder={'Иванов Иван Иванович'}/>
            </label>
            <label htmlFor={'Mac_field'} className={'MacForm'}>Mac-address: <br/>
                <input type={'text'} id={'Mac_field'} name={'MAc-field'} className={'MacInput'} pattern={'[A-Z0-9]{2}-[A-Z0-9]{2}-[A-Z0-9]{2}-[A-Z0-9]{2}-[A-Z0-9]{2}-[A-Z0-9]{2}'} placeholder={'AA-AA-AA-AA-AA-AA'}/>
            </label>
            <label htmlFor={'Mail_field'} className={'MailForm'}>Mail:<br/>
                <input type={'email'} id={'Mail_field'} name={'Mail_field'} className={'MailInput'} placeholder={'example@example.com'}/>
            </label>
            <label htmlFor={'Amount_field'} className={'AmountForm'}>Сумма:<br/>
                <input type={'number'} max={'10000'} id={'Amount_field'} name={'Amount_field'} className={'AmountInput'} placeholder={'99999999'}/>
            </label>
            {this.RequestButton()}
        </form>)
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

