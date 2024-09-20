-- website -> https://www.adamchoi.co.uk/overs/detailed
function main(splash, args)
 -- Change User-Agent (Option 1)
    --splash: set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")

    -- Change User-Agent (Option 2)
    --[[
        headers = {
        [
            'User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    splash: set_custom_headers(headers)
            - -]]

    -- Change User-Agent (Option 3)
    splash: on_request(function(request)
    request: set_header('User-Agent',
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36')
    end)
    -- If a website doesn't render correctly, disabling Private mode might help
  splash.private_mode_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(3))
  buttons = assert(splash:select_all('label.btn-primary'))
  buttons[2]:mouse_click()
  assert(splash:wait(3))
  	-- Increase the viewport to make all the content visible
  splash:set_viewport_full()
  return {splash:png(), splash:html()}
end
