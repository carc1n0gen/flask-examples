import React, { useEffect, useState } from 'react';
import { Helmet } from 'react-helmet';
import { useLocation } from 'react-router-dom';

function getPageTitle(path) {
  switch(path) {
    case '/':
      return 'Flask React!';
    case '/about':
      return 'About - Flask React!';
  }
}

export default function() {
  const location = useLocation();
  return (
    <Helmet>
      <title>{getPageTitle(location.pathname)}</title>
    </Helmet>
  );
}
