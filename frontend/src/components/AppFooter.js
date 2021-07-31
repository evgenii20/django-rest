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

const Footer = () => {
    return <footer>
        <div>
            {/*{menu.map((value, index) => {*/}
            {/*    return <div key={index}><a name={value}/></div>*/}
            {/*})}*/}
            <div>obout</div>
            <div>phone</div>
            <div>email</div>
        </div>
    </footer>
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

export default Footer