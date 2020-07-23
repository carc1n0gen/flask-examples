import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import { Link, useLocation } from 'react-router-dom';

export default function() {
  const { pathname } = useLocation();
  return (
    <Navbar bg="light" expand="lg">
      <Navbar.Brand as={Link} href="/" to="/">Flask React</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav activeKey={pathname}>
          <Nav.Link as={Link} href="/" to="/">Home</Nav.Link>
          <Nav.Link as={Link} href="/about" to="/about">About</Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}
