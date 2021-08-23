import React from 'react'
import Project from "./Project";


const ProjectItem = ({project, users, deleteProject}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.text}</td>
            {/*<td>*/}
            {/*    {project.users.map((userID) => {*/}
            {/*        return users.find((user) => user.id == userID).last_name*/}
            {/*    }).join(', ')}*/}
            {/*</td>*/}
            <td>
                {/*{project.users.map((userID) => {*/}
                {/*    let user = users.filter((user) => user.id === userID)*/}
                {/*    if (user) {*/}
                {/*        return users.find((user) => user.id === userID).last_name*/}
                {/*       // console.log(users.filter((user) => user.id == userID).last_name)*/}
                {/*    }*/}
                {/*}).join(', ')*/}
                {/*}*/}

                {project.users.map((userID) => {
                    let user = users.find((user) => user.id == userID)
                    console.log('user', user)
                    if (user) {

                        return user.last_name
                    }
                })}

            </td>
            <td><button onClick={() => deleteProject(project.id)} type='button'>Delete</button></td>
        </tr>
    )
}

//Поднимаем на верх deleteProject в App
const ProjectList = ({projects, users, deleteProject}) => {
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                Name
            </th>
            <th>
                Text
            </th>
            <th>
                Users
            </th>
            {projects.map((project) => <ProjectItem project={project} users={users} deleteProject={deleteProject}/>)}
        </table>
    )
}

export default ProjectList