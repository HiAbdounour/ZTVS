insert into public.authorized_emails (email)
values ('personne@example.com')
on conflict (email) do nothing;
