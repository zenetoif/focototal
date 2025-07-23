from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Pessoa, Cronograma, Recompensa, SessaoPomodoro, Relatorio, Dica, MaterialApoio


# Inline para Cronogramas dentro da Pessoa
class CronogramaInline(admin.TabularInline):
    model = Cronograma
    extra = 1
    fields = ('titulo', 'data', 'hora_inicio', 'hora_fim', 'publico')
    show_change_link = True
    ordering = ('-data', 'hora_inicio')


@admin.action(description="Marcar selecionados como públicos")
def marcar_publico(modeladmin, request, queryset):
    queryset.update(publico=True)


@admin.action(description="Marcar selecionados como privados")
def marcar_privado(modeladmin, request, queryset):
    queryset.update(publico=False)


@admin.register(Cronograma)
class CronogramaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'link_pessoa', 'data', 'hora_inicio', 'hora_fim', 'publico')
    list_filter = ('publico', 'data', 'pessoa')
    search_fields = ('titulo', 'descricao', 'pessoa__nome_completo')
    ordering = ('-data', 'hora_inicio')
    date_hierarchy = 'data'
    actions = [marcar_publico, marcar_privado]
    list_per_page = 25
    list_select_related = ('pessoa',)

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('pessoa', 'titulo', 'descricao')
        }),
        ('Detalhes do Agendamento', {
            'fields': (('data', 'hora_inicio', 'hora_fim'),)
        }),
        ('Configurações Avançadas', {
            'fields': ('publico',)
        }),
    )

    def link_pessoa(self, obj):
        if obj.pessoa:
            url = reverse('admin:app_pessoa_change', args=[obj.pessoa.id])
            return format_html('<a href="{}">{}</a>', url, obj.pessoa.nome_completo)
        return "-"
    link_pessoa.short_description = 'Pessoa'


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'user', 'email_usuario', 'pontos', 'total_cronogramas')
    search_fields = ('nome_completo', 'user__username', 'user__email')
    ordering = ('nome_completo',)
    inlines = [CronogramaInline]

    def email_usuario(self, obj):
        return obj.user.email
    email_usuario.short_description = 'E-mail'

    def total_cronogramas(self, obj):
        return obj.cronograma_set.count()
    total_cronogramas.short_description = 'Nº Cronogramas'


@admin.register(Recompensa)
class RecompensaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'pessoa', 'pontos_custo', 'resgatada', 'data_obtida', 'descricao_curta')
    list_filter = ('data_obtida', 'resgatada')
    search_fields = ('titulo', 'descricao', 'pessoa__nome_completo')
    ordering = ('-data_obtida',)
    list_per_page = 25

    def descricao_curta(self, obj):
        if obj.descricao and len(obj.descricao) > 50:
            return obj.descricao[:47] + '...'
        return obj.descricao
    descricao_curta.short_description = 'Descrição'


@admin.register(SessaoPomodoro)
class SessaoPomodoroAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'data', 'duracao', 'pausas')
    list_filter = ('data', 'pessoa')
    ordering = ('-data',)
    search_fields = ('pessoa__nome_completo',)
    list_per_page = 25


@admin.register(Relatorio)
class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'data', 'total_pomodoros', 'tempo_total', 'observacoes_curta')
    list_filter = ('data', 'pessoa')
    search_fields = ('pessoa__nome_completo', 'observacoes')
    ordering = ('-data',)
    list_per_page = 25

    def observacoes_curta(self, obj):
        if obj.observacoes:
            return obj.observacoes[:40] + '...' if len(obj.observacoes) > 40 else obj.observacoes
        return '-'
    observacoes_curta.short_description = 'Observações'


@admin.register(Dica)
class DicaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo', 'conteudo')
    list_per_page = 25


@admin.register(MaterialApoio)
class MaterialApoioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'link_externo', 'imagem_preview')
    search_fields = ('titulo', 'descricao')
    list_per_page = 25

    def link_externo(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.link, obj.link)
    link_externo.short_description = 'Link'

    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html(
                '<img src="{}" style="max-height: 60px; max-width: 120px; border-radius: 8px;" />',
                obj.imagem
            )
        return '-'
    imagem_preview.short_description = 'Imagem'
