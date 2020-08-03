import React from 'react';
import ReactDOM from 'react-dom';
import '../css/auth.css';

function AuthPage(props) {
    return (
        <div>
            <Header/>
            <Main/>
            <Footer/>
        </div>
    )
}

function Header(props) {
    return <header className={'header'}><Logo/></header>;
}

function Logo(props) {
    return <a className={'Logo'} href={"#main_page"}>GoToCredit</a>;
}

function Main(props) {
    return <main className={'main'}><Inner_container/></main>;
}

function Inner_container(props) {
    return <div className={'inner_container'}>
        <ContainerTitle/>
        <ContainerText/>
        <ButtonBox/>
    </div>;
}

function ContainerTitle(props) {
    return <h1 className={'container_title'}>GoToCredit</h1>
}

function ContainerText(props) {
    return <h2 className={'container_text'}>Всего 3 шага до вашей мечты!</h2>
}

function Footer(props) {
    return <footer className={'footer'}><Footer_text/></footer>;
}

function Footer_text(props) {
    return <h3 className={'footer_text'}>По всем вопросам писать сюда - @tvorogme</h3>;
}


function LoginButton(props) {
    return <a className={'LoginButton'} value={'login'} href={"#main_page"}>Login</a>;
}

function RegisterButton(props) {
    return <a className={'RegisterButton'} value={'register'}  href={"https://stonks.goto.msk.ru/o/authorize/?state=random_state_string&client_id=M2mY5d4b6NcVKxr2XqKXSxZgpk78WK6ZaU3IxYDd&"}>
        Register
    </a>;
}

function ButtonBox(props) {
    return <div className={'ButtonBox'}>
        <RegisterButton/>
        <LoginButton/>
    </div>;
}

ReactDOM.render(<AuthPage/>, document.getElementById('cool'));
