import React from 'react'
// import * as ReactDOM from "react-dom";
import {Link} from "react-router-dom"
import './../bootstrap/css/bootstrap.min.css'
// import './../App' from is_authenticated
// import APIUser from "./APIUser";

// let menu = [
//     'GET',
//     'POST',
//     'PUT',
//     'DELETE',
//     'OPTIONS',
//     'HEAD',
//     'PATCH',
// ]

const HeaderMenu = () => {

    // return <header className="AppHeader">
    return <header>
        <nav className="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            {/*{menu.map((value, index) => {*/}
            {/*    return <div key={index}><a name={value}/></div>*/}
            {/*})}*/}
            <a className="navbar-brand" href="#">DRF</a>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse"
                    aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarCollapse">
                {/*<ul className="list-style">*/}
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item active"><Link className="nav-link" to='/'>Пользователи</Link></li>
                    <li className="nav-item active"><Link className="nav-link" to='/projects'>Проекты</Link></li>
                    <li className="nav-item active"><Link className="nav-link" to='/projects/create'>Создать проект</Link></li>
                    <li className="nav-item active"><Link className="nav-link" to='/todo/create'>Создать todo</Link></li>
                    <li className="nav-item active"><Link className="nav-link" to='/todo'>Заметки</Link></li>
                    <li className="nav-item active"><Link className="nav-link" to='/login'>Вход</Link></li>
                    <li className="nav-item active"><Link className="nav-link" to='/logout'>Выход</Link> </li>
                    {/*<li>*/}
                    {/*    {this.is_authenticated() ? <button onClick={() => this.logout()}>Выход</button> :*/}
                    {/*        <Link to='/login'>Вход</Link>}*/}
                    {/*</li>*/}
                    {/*<li className="nav-item active">*/}
                    {/*    <button onClick={() => this.logout()}>Выход</button>*/}
                    {/*</li>*/}
                </ul>
            </div>
        </nav>
    </header>
}

// const Link = () => {
//     const url = '/' + this.props.label.toLowerCase().trim().replace(" ", "-");
//
//     return <div>
//         <a href={url}>{this.props.label}</a>
//     </div>
// }
// class Link extends React.Component {
//     render() {
//         const url = '/' + this.props.label.toLowerCase().trim().replace(" ", "-");
//         return <div><a href={url}>
//             {
//                 this.props.label
//             }
//         </a>
//         </div>
//
//     }
// }

export default HeaderMenu