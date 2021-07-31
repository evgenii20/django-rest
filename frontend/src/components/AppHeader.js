import React from 'react'
import * as ReactDOM from "react-dom";

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
    return <header>
        <div>
            {/*{menu.map((value, index) => {*/}
            {/*    return <div key={index}><a name={value}/></div>*/}
            {/*})}*/}
            <div><a>GET</a></div>
            <div><a>POST</a></div>
            <div><a>PUT</a></div>
        </div>
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