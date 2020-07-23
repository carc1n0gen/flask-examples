import React, {useState} from 'react';
import { BrowserRouter as Router, Link, Switch, Route } from 'react-router-dom';
import { Container } from 'react-bootstrap';
import { Home, About, NotFound } from '../Pages';
import Helmet from './Helmet';
import Nav from './Nav';

export default function App() {
  return (
    <Router>
      <Helmet />
      <Nav />
      <Container as="main">
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/about">
            <About />
          </Route>
          <Route>
            <NotFound />
          </Route>
        </Switch>
      </Container>
    </Router>
  )
};
