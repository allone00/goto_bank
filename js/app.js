import React from 'react';
import ReactDOM from 'react-dom';


function AuthPage(props) {
    return (
        <div>
        <Header></Header>
        <Main></Main>
        <Footer></Footer>
        </div>
)}

function Header(props) {
    return <header className={'header'}><Logo></Logo></header>;
}

function Logo(props) {
    return <a className={'Logo'} href={"#main_page"}>GoToCredit</a>;
}

function Main(props) {
    return <main className={'main'}><Inner_container></Inner_container></main>;
}

function Inner_container(props) {
    return <div className={'inner_container'}>
        <ContainerTitle></ContainerTitle>
        <ContainerText></ContainerText>
        <ButtonBox>
            <RegisterButton></RegisterButton>
            <LoginButton></LoginButton>
        </ButtonBox>
    </div>;
}

function ContainerTitle(props) {
    return <h1 className={'container_title'}>GoToCredit</h1>
}

function ContainerText(props) {
    return <h2 className={'container_text'}>Всего 3 шага до вашей мечты!</h2>
}

function Footer(props) {
    return <footer className={'footer'}><Footer_text></Footer_text></footer>;
}

function Footer_text(props) {
    return <h3 className={'footer_text'}>По всем вопросам писать сюда - @tvorogme</h3>;
}


function LoginButton(props) {
    return <button className={'LoginButton'} type={'submit'} value={'login'}>Login</button>;
}

function RegisterButton(props) {
    return <button className={'RegisterButton'} type={'submit'} value={'register'}>Register</button>;
}

const ButtonBox = () => <div className={'ButtonBox'}></div>;

ReactDOM.render(<AuthPage/>, document.querySelector('body'));