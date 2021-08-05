import React from 'react'
import Project from "./Project";


const ProjectItem = ({project, users}) => {
    return (
        <tr>
            <td>
                {project.id}
            </td>
            <td>
                {project.name}
            </td>
            <td>
                {project.text}
            </td>
            <td>
                {project.users.map((userID) => {
                    return users.find((user) => user.id == userID).last_name
                }).join(', ')}
            </td>
        </tr>
    )
}

const ProjectList = ({projects, users}) => {
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
            {projects.map((project) => <ProjectItem project={project} users={users}/>)}
        </table>
    )
}

export default ProjectList