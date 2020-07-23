import React, {useEffect, useState} from 'react';
import { Table } from 'react-bootstrap';

export default function Home() {
  const [people, setPeople] = useState([])
  
  async function getPeople() {
    const response = await fetch('/api/people');
    setPeople(await response.json())
  }

  useEffect(() => {
    getPeople();
  }, []);

  return <>
    <p>This table data is loaded through a fetch call to the flask backend!</p>
    <Table hover>
      <thead>
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        {people.map(person => (
          <tr key={person.id}>
            <td>{person.id}</td>
            <td>{person.name}</td>
            <td>{person.status}</td>
          </tr>
        ))}
      </tbody>
    </Table>
  </>
}
