import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/blog',
    component: ComponentCreator('/blog', 'e2b'),
    exact: true
  },
  {
    path: '/blog/archive',
    component: ComponentCreator('/blog/archive', '182'),
    exact: true
  },
  {
    path: '/blog/test',
    component: ComponentCreator('/blog/test', '1c3'),
    exact: true
  },
  {
    path: '/markdown-page',
    component: ComponentCreator('/markdown-page', '3d7'),
    exact: true
  },
  {
    path: '/docs',
    component: ComponentCreator('/docs', '8a3'),
    routes: [
      {
        path: '/docs',
        component: ComponentCreator('/docs', '253'),
        routes: [
          {
            path: '/docs',
            component: ComponentCreator('/docs', '1af'),
            routes: [
              {
                path: '/docs/',
                component: ComponentCreator('/docs/', '4a8'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
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
