import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', '5ff'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '5ba'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', 'a2b'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', 'c3c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '156'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', '88c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '000'),
    exact: true
  },
  {
    path: '/markdown-page',
    component: ComponentCreator('/markdown-page', '3d7'),
    exact: true
  },
  {
    path: '/docs',
    component: ComponentCreator('/docs', '0e7'),
    routes: [
      {
        path: '/docs',
        component: ComponentCreator('/docs', '133'),
        routes: [
          {
            path: '/docs',
            component: ComponentCreator('/docs', '0e9'),
            routes: [
              {
                path: '/docs/api/',
                component: ComponentCreator('/docs/api/', '5e5'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/api/constants',
                component: ComponentCreator('/docs/api/constants', 'd5f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/api/generate',
                component: ComponentCreator('/docs/api/generate', '188'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/api/models',
                component: ComponentCreator('/docs/api/models', '902'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/api/parse',
                component: ComponentCreator('/docs/api/parse', '44d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/api/render',
                component: ComponentCreator('/docs/api/render', 'e20'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/',
    component: ComponentCreator('/', 'e5f'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
