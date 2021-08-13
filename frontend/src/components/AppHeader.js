import React from 'react'
// import * as ReactDOM from "react-dom";
import {Link} from "react-router-dom"

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
    return <header className="AppHeader">
        <nav>
            {/*{menu.map((value, index) => {*/}
            {/*    return <div key={index}><a name={value}/></div>*/}
            {/*})}*/}
            <ul className="list-style">
                <li><Link to='/'>Пользователи</Link></li>
                <li><Link to='/projects'>Проекты</Link></li>
                <li><Link to='/todo'>Заметки</Link></li>
                <li><Link to='/login'>Вход</Link></li>
                {/*<li>*/}
                {/*    {this.is_authenticated() ? <button onClick={() => this.logout()}>Выход</button> :*/}
                {/*        <Link to='/login'>Вход</Link>}*/}
                {/*</li>*/}
                <li>
                    <button onClick={() => this.logout()}>Выход</button>
                </li>
            </ul>
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