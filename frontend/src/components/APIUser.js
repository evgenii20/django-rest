import React from 'react'
import APIUser from "./APIUser";
import {Link} from "react-router-dom";


const APIUserItem = ({user}) => {
    // return (
    //     <tr>
    //         <td>
    //             {user.id}
    //         </td>
    //         <td>
    //             {user.first_name}
    //         </td>
    //         <td>
    //             {user.last_name}
    //         </td>
    //         <td>
    //             {user.email}
    //         </td>
    //     </tr>
    // )
    return (
        <tr>
            {/*<td>*/}
            {/*    <Link to={`users/${user.id}`}>{user.id}</Link>*/}
            {/*</td>*/}
            <td>
                {user.first_name}
            </td>
            <td>
                <Link to={`users/${user.id}`}>{user.last_name}</Link>
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const APIUserList = ({users}) => {
    return (
        <table>
            {/*<th>*/}
            {/*    ID*/}
            {/*</th>*/}
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                E-mail
            </th>
            {/*{users.map((user) => <AuthorItem author={user} />)}*/}
            {users.map((user) => <APIUserItem user={user}/>)}
        </table>
    )
}

export default APIUserList