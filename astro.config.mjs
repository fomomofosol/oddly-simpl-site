// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
	site: 'https://oddlysimpl.xyz',
	integrations: [mdx(), sitemap()],
	output: 'static',
	image: {
		service: {
			entrypoint: 'astro/assets/services/sharp',
			config: {},
		},
	},
});
