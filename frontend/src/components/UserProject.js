import React from 'react'
import { useParams } from 'react-router-dom'


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
                {/*{project.users.name}*/}
                {/*{project.users}*/}
                {project.users.map((userID) => {
                    return users.find((user) => user.id == userID).last_name
                }).join(', ')}
            </td>
        </tr>
    )
}

const ProjectList = ({projects, users}) => {
    let { id } = useParams();
    // let filtered_projects = projects.filter((project) => project.users.name === id)
    let filtered_projects = projects.filter((project) => project.users.includes(parseInt(id)))
    // let filtered_projects = projects.filter((project) => {
    //     console.log(id)
    //     console.log(project.users)
    //     console.log(project.users.id)
    //     return project.users.includes(parseInt(id));
    // })
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
            {/*{projects.map((project) => <ProjectItem project={project}/>)}*/}
            {filtered_projects.map((project) => <ProjectItem project={project} users={users}/>)}
        </table>
    )
}

export default ProjectList