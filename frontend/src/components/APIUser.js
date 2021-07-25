import React from 'react'
import APIUser from "./APIUser";


const APIUserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
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